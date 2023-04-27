# Memory/Cache hierarchy Optimizations for Graph Analytics (Team Memory Maestros)
|      Name    |  Roll No. |
|     :---     |   :----   |
| Harsh Vardhan | 210050064 |
| Hitesh Kumar | 210050066 |

## The goals of the project
* Improve memory performance on graph-based workloads 
* Decrease overall latency of cache access by improving cache organization system 

## What we have done in the code
We have implemented the inclusivity in the cache memory hierarchy using the main_inclusive and check_inclusive function.

### What does the main_inclusive function implemented by us do in src/cache.cc?
The purpose of this function is to implement an inclusive cache policy, which means that when a block is brought into a higher-level cache, all copies of the block in lower-level caches must be invalidated.

Here is a breakdown of this part of the code:
1. The function takes several inputs, including the CPU ID (`cpu`), the eviction CPU ID (`evict_cpu`), a reference to the cache (`cache`), the memory address (`address`), and the instruction ID (`instr_id`).
2. If the MSHR (Miss Status Holding Register) occupancy is not zero, the function checks if there is an outstanding request for the memory block with the given address in the MSHR. If so, it returns false, indicating that the cache cannot be made inclusive yet.
3. If the cache is an L2 cache (`cache_type == IS_L2C`) and the WQ (Write Queue) occupancy is not zero, the function checks if there is a pending writeback request for the memory block with the given address in the WQ. If so, it returns false, indicating that the cache cannot be made inclusive yet.
4. The function calculates the set index (`set`) for the given memory address using the `get_set` function.
5. The function loops through all the ways in the cache (`NUM_WAY`) for the given set. For each way, the function checks if the tag matches the memory address and the block is valid.
6. If the block is dirty (i.e., it has been modified), the function checks if the cache has a lower-level cache (`lower_level`). If so, it checks if the lower-level cache's occupancy is full for the set and address of the block. If the occupancy is full, it increments the `WQ_FULL` counter and returns false, indicating that the cache cannot be made inclusive yet.
7. If the lower-level cache's occupancy is not full, the function creates a `writeback_packet` to write the modified block back to the lower-level cache. The packet includes various information about the block, such as the fill level, CPU ID, address, data, and type of the packet.
8. The function adds the `writeback_packet` to the lower-level cache's WQ using the `add_wq` function.
9. The function sets the block's valid bit to 0, indicating that the block has been invalidated in the current cache.
10. If the block is not dirty, the function simply sets the block's valid bit to 0.
11. The function returns true, indicating that the cache has been made inclusive successfully.

In short, this code implements an inclusive cache policy by checking for outstanding requests and pending writebacks, and invalidating any copies of the memory block in lower-level caches when a block is modified in a higher-level cache.

### Changes in the handle_fill function in the src/cache.cc function
The code implemented in the handle_fill does the following:

1. When a block is evicted from the Last Level Cache (LLC) or L2 Cache (L2C) based on the value of `cache_type`, the code checks if it is a valid block. If it is a valid block, the code then checks each CPU for inclusivity using the `make_inclusive` function.
2. If the block is inclusive in all CPUs, then `do_fill` is set to 1, indicating that the block can be filled in the cache hierarchy. If the block is not inclusive in any of the CPUs, `do_fill` is set to 0, and the `STALL` counter for the respective type of MSHR entry is incremented.
3. The `make_inclusive` function checks if the given CPU's cache hierarchy (L1I, L1D, L2C) already contains the block. If it does, the block is marked as inclusive in the respective cache, and `make_inclusive` returns 1. Otherwise, `make_inclusive` returns 0.
4. If the eviction is done at the L2C level and the block is not inclusive in the local CPU's L1I and L1D caches, `do_fill` is set to 0, and the `STALL` counter for the respective type of MSHR entry is incremented.

### Changes in the handle_writeback function in the src/cache.cc function
The code I implemented in the handle_writeback do the following:

1. The implemented code is responsible for handling cache evictions in the `handle_writeback` function. It checks if the block being evicted is valid and then checks if it needs to be made inclusive in any other caches (L1I, L1D, and L2C) for other processors in a multi-core system.
2. The code first checks if the cache type is LLC and the block being evicted is valid. If so, it iterates over all processors and checks if the block needs to be made inclusive in any L1I or L1D caches using the `make_inclusive` function. If making the block inclusive fails for any of the caches, then the `do_fill` flag is set to 0 and the `STALL` counter for the eviction type is incremented.
3. Next, the code checks if the cache type is L2C and the block being evicted is valid. If so, it checks if the block needs to be made inclusive in any L1I or L1D caches for the current processor using the `make_inclusive` function. If making the block inclusive fails, then the `do_fill` flag is set to 0 and the `STALL` counter for the eviction type is incremented.
4. Overall, this code ensures that any blocks being evicted from the LLC or L2C caches are made inclusive in any L1I, L1D, and L2C caches that might hold the same block for other processors.

### And finally what does the check_inclusive function implemented by us do in src/cache.cc?
1. The code in this function is performing checks to ensure cache inclusivity, which means that a higher-level cache (e.g., L2C or LLC) should contain all the data present in lower-level caches (e.g., L1I or L1D). 
2. The function iterates over all CPUs and cache blocks and verifies that each block's address is present in the L2C and LLC caches. If a block is present in the L1I or L1D caches and not present in the higher-level caches, a message is printed to the console, indicating that the data is missing. 
3. The code also checks if the block is dirty and not present in the higher-level caches. If it finds a block that is dirty, it prints a message stating that the dirty block is not present in the L2C or LLC. 
4. Finally, the code checks if there are any blocks present in L1I or L1D but not present in the L2C or LLC caches, and it reports the number of such blocks found.

The two new functions `main_inclusive` and the `check_inclusive` are both declared in the `cache.h` and the `check_inclusive` function is called from the `main.cc`
