"""
Name: CS3853 Team 13 Project M#1 Summer 2020
Date: 06/28/2020

Author: Jackson Dumas (llt190)
Author: Molly Pena (tcg202)
Author: Humberto Gonzalez (tve794)

Purpose: This is the first module for the cache simulation project

Notes: N/A
"""

import os
import sys
import math

from CacheResults import *
from main import *
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


def cache_info(size, b_size, pway, rep_alg):
    # print input parameters
    global cacheInfo
    cacheInfo = {}
    print("\n***** Cache Input Parameters *****")
    print("Cache Size:\t\t" + str(size) + "KB")
    print("Block Size:\t\t" + str(b_size) + " bytes")
    print("Associativity:\t\t" + str(pway))

    # Check the replacement algorithm
    if (rep_alg == "RR"):
        print("Replacement Policy:\t" + "Round Robin")
    elif (rep_alg == "RND"):
        print("Replacement Policy:\t" + "Random")
    elif (rep_alg == "LRU"):
        print("Replacement Policy:\t" + "Least Recently Used")

    # calculate and print cache stats
    cost_per_kb = 0.07
    total_blocks = (1024 * size) / b_size
    total_rows = (1024 * size) / (b_size * pway)
    block_offset = math.log2(b_size)
    index_size = (math.log2(size) + 10)  - math.log2(b_size * pway)
    tag_size = 32 - block_offset - index_size
    overhead_size = ((tag_size + 1) * total_blocks) / 8
    imp_size = (1024 * size) + overhead_size
    total_cost = round((imp_size / 1024) * cost_per_kb, 2)

    print("\n***** Cache Calculated Values *****")
    print("Total # Blocks:\t\t" + str(total_blocks))
    print("Tag Size:\t\t" + str(tag_size))
    print("Index Size:\t\t" + str(index_size))
    print("Total Rows:\t\t" + str(total_rows))
    print("Overhead Size:\t\t" + str(overhead_size) + " bytes")
    print("Implementation Size:\t" + str(imp_size / 1024) + "KB (" + str(imp_size) + "bytes)")
    print("Total Cost:\t\t" + str(total_cost))

    cacheInfo["OverHead_size"] = overhead_size
    cacheInfo["Total_blocks"] = total_blocks
    cacheInfo["Block_size"] = b_size
    cacheInfo["Imp_size"] = imp_size

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
    global block_size
    global associativity
    global cache_size
    if (len(sys.argv) == 11):  # Trace file included
        file_name = sys.argv[2]  # Assign trace file name
        cache_size = int(sys.argv[4])  # Assign cache size cast to int
        block_size = int(sys.argv[6])  # Assign block size cast to int
        associativity = int(sys.argv[8])  # Assign associativity cast to int
        replacement = sys.argv[10]  # Assign replacement algorithm

        # Check that trace file exists
        if not os.path.isfile(file_name):
            print("Error: the trace file does not exist")
            sys.exit(-1)
        print("Trace File: " + file_name)
    elif (len(sys.argv) == 9):  # Trace file not included
        cache_size = int(sys.argv[2])
        block_size = int(sys.argv[4])
        associativity = int(sys.argv[6])
        replacement = sys.argv[8]

    # Calculate and Print Cache stats
    cache_info(cache_size, block_size, associativity, replacement)



"""
Function: parse_trc_file

Purpose:
    For M1, it simply reads each line of the trace file,
    parses it, and prints the address instruction and length
    in the format 0x0000000 (length)

Notes:
    For M1, this only reads 20 lines
"""


def parse_trc_file(filename):
    global cnt
    global firstBlock
    firstBlock = {}
    global instInMem
    instInMem = []
    global eip
    eip = 0
    global tokens
    tokens = []
    global num_instructions
    global total_length
    global hit
    hit = 0
    global miss
    miss = 0
    total_length = 0
    num_instructions = 0
    # Check that trace file exists

    firstBlock["eb3"] = "7c81"
    if not os.path.isfile(filename):
        print("Error: the trace file does not exist")
        sys.exit(-1)

    try:  # try opening the file and catch any IO exception
        with open(filename, 'r') as tracefile:
            line = tracefile.readline()
            cnt = 0
            while line and cnt >= 0:  # read until EOF or until line 20
                tokens = line.split()  # tokenize the line into a list of strings
                #print(line)
                if len(tokens) > 0 and tokens[0] == "EIP":  # check for empty or unrelated lines
                    inst_addr = tokens[2]  # third element of each line is the address
                    instr_len = tokens[1].strip("(:)")  # second element is the length with padded parenthesis and colon
                    cnt += 1

                    EIP = tokens[1]
                    EIP = int(EIP[1:3])

                    hexAdress = tokens[2]
                    index = hexAdress[4:7]
                    tag = hexAdress[0:4]
                    eip += 1

                    if index in firstBlock:
                        if firstBlock[index] != tag:
                            firstBlock[index] = tag
                            miss +=1
                        if firstBlock[index] == tag:
                            hit +=1
                    else:
                        firstBlock[index] = tag
                        miss +=1

                elif len(tokens) > 0 and tokens[0] == "dstM:":

                    write_addr = tokens[1]
                    if write_addr != "00000000":
                        eip += 1


                    read_addr = tokens[4]
                    if read_addr != "00000000":
                        eip += 1





                line = tracefile.readline()  # read the next line


    except IOError:
        print("Error: could not open trace file")
        sys.exit(-1)


def rr(filename):
    global cnt
    eip = 0
    global num_access
    num_access = 0
    global secondBlock
    secondBlock = {}
    global firstBlock
    firstBlock = {}
    global instInMem
    instInMem = []
    global num_addresses
    num_addresses = 0
    global tokens
    tokens = []
    global num_instructions
    global total_length
    global hit
    hit = 0
    global compulssory_miss
    compulssory_miss = 0
    global conflict_miss
    conflict_miss = 0
    total_length = 0
    num_instructions = 0
    # Check that trace file exists

    firstBlock["eb3"] = "7c81"
    if not os.path.isfile(filename):
        print("Error: the trace file does not exist")
        sys.exit(-1)

    try:  # try opening the file and catch any IO exception
        with open(filename, 'r') as tracefile:
            line = tracefile.readline()
            cnt = 0
            while line and cnt >= 0:  # read until EOF or until line 20
                tokens = line.split()  # tokenize the line into a list of strings
                #print(line)
                if len(tokens) > 0 and tokens[0] == "EIP":  # check for empty or unrelated lines
                    inst_addr = tokens[2]  # third element of each line is the address
                    instr_len = tokens[1].strip("(:)")  # second element is the length with padded parenthesis and colon
                    cnt += 1

                    EIP = tokens[1]
                    EIP = int(EIP[1:3])
                    eip +=EIP

                    hexAdress = tokens[2]
                    index = hexAdress[4:7]
                    tag = hexAdress[0:4]
                    num_addresses += 1

                    # if index is in first  block of 2 way associative
                    if index in firstBlock:
                        num_access +=1
                        # if the tag in index is not equal to tag check the second block
                        if firstBlock[index] != tag:
                            num_access +=1
                            # if the index contains the tag it is a hit
                            if index in secondBlock:

                                if secondBlock[index] == tag:
                                    num_access += 1
                                    hit +=1
                    # if the tag in the index does not = to tag then its a conflict miss
                                elif secondBlock[index] != tag:
                                    num_access += 1
                                    secondBlock[index] = tag
                                    conflict_miss +=1
                            # if the index doesnt contain the tag then its a compulsory miss
                            # add the tag to the block at that index
                            elif index not in secondBlock:
                                num_access += 1
                                secondBlock[index] = tag
                                compulssory_miss +=1


                            firstBlock[index] = tag
                            compulssory_miss +=1

                        elif firstBlock[index] == tag:
                            hit += 1





                    # if not in the first block then its a compulsory miss
                    # add index and data to first block
                    elif index not in firstBlock:
                        firstBlock[index] = tag
                        compulssory_miss +=1




                elif len(tokens) > 0 and tokens[0] == "dstM:":

                    write_addr = tokens[1]
                    if tokens[1] != "00000000":
                        num_addresses += 1




                    read_addr = tokens[4]
                    if read_addr != "00000000":
                        num_addresses += 1





                line = tracefile.readline()  # read the next line
        cacheInfo["eip"] = eip

    except IOError:
        print("Error: could not open trace file")
        sys.exit(-1)



"""
Function: main

Purpose:
    Entrypoint to the program
"""


def main():
    # print team information
    print("Cache Simulator CS3853 Summer 2020 - Group #13\n")

    parse_args()
   # parse_trc_file(sys.argv[2])


    rr((sys.argv[2]))
    printCacheResults(hit,compulssory_miss, conflict_miss, num_addresses, num_access, cacheInfo)


if __name__ == "__main__":

    main()

