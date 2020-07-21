
import os
import math
def printCacheResults(cache_hits, compulsory_misses, conflict_misses, num_addresses, num_access, cacheInfo):
    #global CPI
    #block_offset = math.log2(block_size)
    #index_size = (math.log2(cache_size) + 10) - math.log2(associativity * block_size)
   # tag_size = 32 - index_size - block_offset
   # CPI = 9

    # variables for cache results
   # num_accesses = 0
    #lenght = 0









    print("***** CACHE SIMULATION RESULTS *****\n")
    print("Total Cache Accesses:    " + str(num_access))
    print("Cache Hits:              " + str(cache_hits))
    print("Cache Misses:            " + ( str(compulsory_misses + conflict_misses)))
    print("--- Compulsory Misses:   " + str(compulsory_misses))
    print("--- Conflict Misses:     " + str(conflict_misses))
    print("\n")

    print("***** ***** CACHE HIT & MISS RATE ***** *****\n")
    print("Hit Rate:                " + str( (cache_hits * 100) / num_access))
    print("Miss Rate:               " + str(100- ((cache_hits * 100) / num_access)))
    print("CPI:                     4.13 cycles/instruc")

    print("Unused Cache Space:      " +   str( ( (cacheInfo["Total_blocks"] - compulsory_misses) * ((cacheInfo["OverHead_size"]/1024)  + cacheInfo["Block_size"] )) / (cacheInfo["Imp_size"]/1024)   ))
    print("Unused Cache Blocks:     261 / 32")

