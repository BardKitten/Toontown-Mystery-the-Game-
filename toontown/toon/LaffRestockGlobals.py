from toontown.toonbase import TTLocalizer

TIMER_SECONDS = 30

# Laff Shop GUI
TIMER_END = 0
USER_CANCEL = 1
RESTOCK = 2

# Restock Results
FULL_LAFF = 0
LESS_LAFF = 1
NOT_ENOUGH_MONEY = 2
RESTOCK_SUCCESSFUL = 3

RestockMessages = {
 FULL_LAFF: TTLocalizer.RestockFullLaffMessage,
 LESS_LAFF: TTLocalizer.RestockLessLaffMessage,
 NOT_ENOUGH_MONEY: TTLocalizer.RestockNoMoneyMessage,
 RESTOCK_SUCCESSFUL: TTLocalizer.RestockSuccessfulMessage
}