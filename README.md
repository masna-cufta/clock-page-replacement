# Clock Page Replacement Algorithm Simulation (Python)

This program simulates the Clock Page Replacement algorithm used in operating systems to manage virtual memory.

## Description

- The simulation models multiple processes, each with a set number of pages.
- There is a limited number of page frames in physical memory.
- Processes randomly access their pages.
- If the requested page is already in a frame (a "hit"), the reference bit for that frame is set to 1.
- If the page is not in a frame (a "miss"), the algorithm looks for a free frame or uses the Clock algorithm to select a victim frame to evict.
- The Clock algorithm moves a pointer (the "clock hand") over the frames and replaces the first frame it finds with a reference bit of 0, resetting reference bits of frames with 1 as it passes.
- The program prints the current state of frames, reference bits, and clock hand position after each access.

## How to Run

Make sure you have Python 3 installed.

Run the program:

```bash
python3 clock_page_replacement.py
```

You can modify the variables at the top of the script (num_processes, pages_per_process, num_accesses, num_frames) to change the simulation parameters.
