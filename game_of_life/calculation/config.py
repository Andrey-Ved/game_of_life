
# CALCULATION_DELAY = 1 / 10**7

if 'CALCULATION_DELAY' not in locals():
    CALCULATION_DELAY = None

CALCULATION_OPTION = 2  # 0 - simple, 1 - with queue, 2 - with map

assert 0 <= CALCULATION_OPTION < 3, \
    'expected that CALCULATION_OPTIONS would be from 0 to 2'

WORKERS_NUMBER = 8