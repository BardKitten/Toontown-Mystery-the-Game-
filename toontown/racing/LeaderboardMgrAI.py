from otp.ai.MagicWordGlobal import *
from toontown.toonbase import TTLocalizer
import RaceGlobals, operator, time

class LeaderboardMgrAI:

    def __init__(self, air):
        self.air = air
        if self.air.dbConn:
            self.air.dbGlobalCursor.leaderboards.ensure_index([('ai', 1)])
            shard = {'ai': self.air.districtId}
            doc = self.air.dbGlobalCursor.leaderboards.find_one(shard)
            if not doc:
                self.database = ({})
            else:
                self.database = doc.get('database', ({}))
            
        else:
            self.database = simbase.backups.load('leaderboard', (self.air.districtId,), default=({}))

    def getDatabase(self):
        return self.database

    def saveDatabase(self):
        if self.air.dbConn:
            shard = {'ai': self.air.districtId}
            self.air.dbGlobalCursor.leaderboards.update(shard,
                                                        {'$setOnInsert': shard,
                                                        '$set': {'database': self.database}},
                                                        upsert = True)
        else:
            simbase.backups.save('leaderboard', (self.air.districtId,), self.database)
        messenger.send('goofyLeaderboardChange')

    def trimList(self, list):
        return list[:RaceGlobals.NumRecordsPerPeriod]

    def clearRace(self, race):
        if race in self.database:
            del self.database[race]
            self.saveDatabase()

    def submitRace(self, raceId, name, timestamp):
        for i in xrange(len(TTLocalizer.RecordPeriodStrings)):
            race = '%s, %s' % (raceId, i)

            if race in self.database:
                originalRace = self.database[race][1]
                newRace = list(originalRace)

                newRace.append([name, timestamp])
                sortedRace = self.trimList(sorted(newRace, key=operator.itemgetter(1)))

                if originalRace != sortedRace:
                    self.database[race][1] = sortedRace
                    self.saveDatabase()
            else:
                self.database[race] = [time.time(), [(name, timestamp)]]
                self.saveDatabase()

@magicWord(category=CATEGORY_PROGRAMMER, types=[str, int, int, str, int])
def leaderboard(command, raceId=0, type=0, name='', time=0):
    command = command.lower()
    race = '%s, %s' % (raceId, type)

    if command == 'clear':
        simbase.air.leaderboardMgr.clearRace(race)
        return 'Cleared race %s!' % race
    elif command == 'submit':
        simbase.air.leaderboardMgr.submitRace(raceId, name, time)
        return 'Submitted race %s for %s with %s seconds!' % (raceId, name, time)
    elif command == 'refresh':
        messenger.send('goofyLeaderboardChange')
        return 'Refreshed leaderboards!'
    elif command == 'change':
        messenger.send('goofyLeaderboardDisplay', [raceId])
        return 'Made all leaderboards show %s!' % raceId
    else:
        return 'Unknown command! Commands:\n- clear\n- submit\n- refresh\n- change'
