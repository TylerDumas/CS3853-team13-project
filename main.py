
"""
Name: CS3853 Team 13 Project M#1 Summer 2020
Date: 06/28/2020

Author: Jackson Dumas (llt190)
Author: 
Author: 

Purpose: This is the first module for the cache simulation project

Notes: N/A
"""

import os
import sys
import math

"""
Function: cache_info

Purpose:
    Calculates and displays all of the necessary
    information about the cache

Params:
    size    |   size of the cache (in KBs)
    b_size  |   size of each block (in bytes)
    pway    |   M-way set associativity
    rep_alg |   string representing the replacement algorithm
"""
def cache_info( size, b_size, pway, rep_alg ):

    #print input parameters
    print( "\n***** Cache Input Parameters *****" )
    print( "Cache Size:\t\t" + str( size ) + "KB" )
    print( "Block Size:\t\t" + str( b_size ) + " bytes" )
    print( "Associativity:\t\t" + str( pway ) )
    
    #Check the replacement algorithm
    if( rep_alg == "RR" ):
        print( "Replacement Policy:\t" + "Round Robin" )
    elif( rep_alg == "RND" ):
        print( "Replacement Policy:\t" + "Random" )
    elif( rep_alg == "LRU" ):
        print( "Replacement Policy:\t" + "Least Recently Used")

    #calculate and print cache stats
    cost_per_kb = 0.07
    total_blocks = (1024 * size) / b_size
    total_rows = (1024 * size) / (b_size * pway)
    block_offset = math.log2( b_size )
    index_size = math.log2( 1024 * (size / (b_size/pway)) )
    tag_size = 32 - block_offset - index_size
    overhead_size = ( (tag_size + 1) * total_blocks ) / 8
    imp_size = (1024 * size) + overhead_size
    total_cost = round( (imp_size / 1024) * cost_per_kb, 2 )

    print( "\n***** Cache Calculated Values *****" )
    print( "Total # Blocks:\t\t" + str(total_blocks) )
    print( "Tag Size:\t\t" + str(tag_size) )
    print( "Index Size:\t\t" + str(index_size) )
    print( "Total Rows:\t\t" + str(total_rows) )
    print( "Overhead Size:\t\t" + str(overhead_size) + " bytes" )
    print( "Implementation Size:\t" + str( imp_size / 1024 ) + "KB (" + str(imp_size) + "bytes)" )
    print( "Total Cost:\t\t" + str( total_cost ) )

"""
Function: parse_args

Purpose: 
    Evaluates the command line arguments and then calls
    the cache_info helper function

Params:
    None

Notes:
    11 total args (including script name),
    9 total args if trace file is omitted
"""
def parse_args():

    if( len( sys.argv ) == 11 ):    #Trace file included
        file_name = sys.argv[2]     #Assign trace file name
        cache_size = int( sys.argv[4] ) #Assign cache size cast to int
        block_size = int( sys.argv[6] ) #Assign block size cast to int
        associativity = int( sys.argv[8] )   #Assign associativity cast to int
        replacement = sys.argv[10]   #Assign replacement algorithm

        #Check that trace file exists
        if not os.path.isfile( file_name ):
            print( "Error: the trace file does not exist" )
            sys.exit( -1 )
        print( "Trace File: " + file_name )
    elif( len( sys.argv ) == 9 ):   #Trace file not included
        cache_size = int( sys.argv[2] )
        block_size = int( sys.argv[4] )
        associativity = int( sys.argv[6] )
        replacement = sys.argv[8]

    #Calculate and Print Cache stats
    cache_info( cache_size, block_size, associativity, replacement )

"""
Function: main

Purpose:
    Entrypoint to the program
"""
def main():
    #print team information
    print( "Cache Simulator CS3853 Summer 2020 - Group #13\n" )
    parse_args()

if __name__=="__main__":
    main()
