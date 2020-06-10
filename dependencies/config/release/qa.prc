# Distribution:
distribution qa

# Art assets:
model-path /

# Server:
server-version SERVER-VERSION-HERE
min-access-level 100
accountdb-type remote
shard-low-pop 50
shard-mid-pop 100

# RPC:
want-rpc-server #t
rpc-server-endpoint http://localhost:8080/

# DClass file is automatically wrapped into the niraidata.

# Core features:
want-pets #t
want-parties #f
want-cogdominiums #t
want-lawbot-cogdo #f
want-anim-props #t
want-game-tables #t
want-find-four #t
want-chinese-checkers #t
want-checkers #t
want-house-types #f
want-gifting #t
want-top-toons #f
want-emblems #f

# Chat:
want-whitelist #t
want-sequence-list #t

# Developer options:
show-population #t
want-instant-parties #f
want-instant-delivery #f
cogdo-pop-factor 1.5
cogdo-ratio 0.5
default-directnotify-level info

# Crates:
dont-destroy-crate #f
get-key-reward-always #f
get-crate-reward-always #f