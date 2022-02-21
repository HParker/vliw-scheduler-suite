# Adam's probably over the top VLIW emulator scheduler test suite (A-Pot-Vests)

This is a suite of tools to assure your VLIW scheduler is scheduling instructions appropriately and your program is generally correct. the suite is comprised of 3 main tools.

## Getting started

1. clone the project
2. copy `vliwScheduler` and your input `.s` file into this directory
3. run one of the provided tools

## The Tools

### `test.sh`

This utility assumes you have an executable `vliwScheduler` in this directory available and runs each of the test input files in the `in` directory. Each test will pass if it's output matches the output in the `expected` directory.

There are two ways to use this tool, use the existing expected files in the `expected` directory. In order to do this, the instructions you output must adhere to the structure,

`<cluster> <operation>, <branch set register if used> = <branch read register if used>, <argument1 or imidiate>, <argument2 or imidiate>`

This requires rewriting all instructions rather than using the input string from the examples in `in`.

The second way to use this tool is to remove everything in `expected`, run `test.sh` then `cp out/* expected` and use this tool to tell if your implementation changed the output for a specific example. This way you can be sure you aren't changing behavior you don't intend to change.

### `output.sh <input file>`

This utility automatically runs `vliwScheduler` with the correct arguments to give you a nice set of VLIW output files for each mode

This will output 7 files:

- 4_wide_critpath_fanout_source_simple.s
- 4_wide_critpath_resource_source_simple.s
- 4_wide_critpath_source_simple.s
- 4_wide_fanout_source_simple.s
- 4_wide_rename_source_simple.s
- 4_wide_resource_source_simple.s
- 4_wide_source_simple.s

### `verifier.sh <compiler_path> <control file>`

This tool will not work without the output from `output.sh`

This tool is a ruby script that verifys that the output of each of the files from `output.sh` return the same output as the control file. run it by running,

```bash
./verifier.sh <path_to_compiler> <control file>
```

you can also run `./verifier.sh` with no arguments and it will guess likely locations for your compiler and control file.

It will compile each of the files from `output.sh` and assure that the output of running the program with `./<test_progarm> 0 1 2 3 4 5 6 7 8 9` returns the same thing as running `./<control_program> 0 1 2 3 4 5 6 7 8 9`.

### `mem_check.sh <input> <output> <mode>`

SUPER IMPORTANT when writing C programs you expect someone else to run to make sure that your memory behavior is reasonable. this also expected a `vliwScheduler` executable in this directory. To use it you must have `valgrind` installed. `sudo apt-get install valgrind` before using this tool.

### `make_submission.sh`

Copy this file into the directory you are doing your project in. It should make/move files needed in the zip into a directory then zip its contents and verify it.

This tool assumes you did not use any subfolders or any files without a `.cpp` or `.h` file extension to run your code. PLEASE VERIFY THE CONTENTS OF THE ZIP FILE YOURSELF. TREAT THIS AS A STARTING POINT.

### `cleanup.sh`

This removes your ta*, gmon* and 4_wide* files.

## Disclaimer

The answers might be wrong! You might fail this course. This software is provided as is and is not an athorative source. No warrent, maintainence or other agreement is implied or given. This code is available under the beerware or MIT license.

```
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <phk@FreeBSD.ORG> wrote this file.  As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return.   Poul-Henning Kamp
 * ----------------------------------------------------------------------------
 */
 ```