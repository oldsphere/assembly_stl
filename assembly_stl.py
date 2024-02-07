#!/bin/env python3
import re
import sys
from os import path
from typing import List
from dataclasses import dataclass, field
from argparse import ArgumentParser


@dataclass
class STLBlock:
    content: str = field(repr=False)
    name: str

    def replace_name(self, new_name: str) -> None:
        self.name = new_name

    def get_stl(self) -> str:
        return f"solid {self.name}\n" f"{self.content}\n" f"endsolid {self.name}\n"


def load_data(filepath: str) -> str:
    """Load the content of the STL file"""
    with open(filepath, "r") as fid:
        return fid.read()


def find_blocks(content: str) -> List[STLBlock]:
    initial_regex = re.compile("^solid (.+)$", re.MULTILINE)
    content_pattern = "solid {block_name}\n(.*)\nendsolid {block_name}"

    blocks = list()
    block_inits = initial_regex.findall(content)
    for block_name in block_inits:
        block_content_pattern = content_pattern.format(block_name=block_name)
        contentMatch = re.search(block_content_pattern, content, re.DOTALL)
        if not contentMatch:
            raise Exception(f'Incomplete block "{block_name}"')
        block = STLBlock(name=block_name, content=contentMatch.group(1))
        blocks.append(block)
    return blocks


def extract_name(filepath: str, prefix: str = "") -> str:
    basename = path.basename(filepath).split(".")[0]
    if prefix:
        return basename.replace(prefix, "")
    return basename


def assembly_stl(blocks: List[STLBlock]) -> str:
    return "\n\n".join([block.get_stl() for block in blocks])


if __name__ == "__main__":

    parser = ArgumentParser(
        prog = "Assembly STL",
        description="Process separated STL files and combine them in a single output"
    )

    parser.add_argument("inlet_files", nargs="+", help="Inlet STL files")
    parser.add_argument("-o", "--output", help="Output STL file")
    parser.add_argument("-p", "--prefix", help="Prefix of the exported STL files")

    args = parser.parse_args()

    inlet_files = args.inlet_files
    output_file = args.output
    prefix = args.prefix

    if not output_file:
        print("No output file provided")
        sys.exit(1)

    blocks = []
    for file in inlet_files:
        content = load_data(file)
        file_blocks = find_blocks(content)
        block_name = extract_name(file, prefix)
        if len(file_blocks) < 1:
            print(f"File {file} has no STL blocks")
            sys.exit(1)
        if len(file_blocks) > 1:
            print(f"File {file} is already a composed STL")
            sys.exit(1)
        block = file_blocks[0]
        block.replace_name(block_name)
        blocks.append(block)

    with open(output_file, "w") as fid:
        fid.write(assembly_stl(blocks))
