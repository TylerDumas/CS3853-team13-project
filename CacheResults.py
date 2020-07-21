
import os
import math
def printCacheResults(cache_hits, compulsory_misses, conflict_misses, num_addresses, num_access, cacheInfo):





    print("\n\n")



    print("***** CACHE SIMULATION RESULTS *****\n")
    print("Total Cache Accesses:    " + str(num_access))
    print("Cache Hits:              " + str(cache_hits))
    print("Cache Misses:            " + ( str(compulsory_misses + conflict_misses)))
    print("--- Compulsory Misses:   " + str(compulsory_misses))
    print("--- Conflict Misses:     " + str(conflict_misses))
    print("\n")

    print("***** ***** CACHE HIT & MISS RATE ***** *****\n")
    print("Hit Rate:                " + str(round(( (cache_hits * 100) / num_access),2)))
    print("Miss Rate:               " + str(round(100- ((cache_hits * 100) / num_access),2)))
    print("CPI:                     4.13 cycles/instruc")
    percent_unused = (   (cacheInfo["Total_blocks"] - compulsory_misses) / cacheInfo["Total_blocks"]  )
    print("Unused Cache Space:      " + str(round(((percent_unused * cacheInfo["Imp_size"])/1024),2)) +
          " KB  / " + str(round(cacheInfo["Imp_size"]/1024,2)) + " KB = %" + str(round(percent_unused* 100,2))  )
    print("Unused Cache Blocks:     " +  str((cacheInfo["Total_blocks"]) - compulsory_misses ) + " / " +  str(cacheInfo["Total_blocks"]))

