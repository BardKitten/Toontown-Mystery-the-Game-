from toontown.toonbase import TTLocalizer

TIMER_SECONDS = 60

# Glove Shop GUI
TIMER_END = 0
USER_CANCEL = 1
CHANGE = 2

# Glove Results
INVALID_COLOR = 0
SAME_COLOR = 1
NOT_ENOUGH_MONEY = 2
CHANGE_SUCCESSFUL = 3

ChangeMessages = {
 INVALID_COLOR: TTLocalizer.GloveInvalidColorMessage,
 SAME_COLOR: TTLocalizer.GloveSameColorMessage,
 NOT_ENOUGH_MONEY: TTLocalizer.GloveNoMoneyMessage,
 CHANGE_SUCCESSFUL: TTLocalizer.GloveSuccessMessage
}
