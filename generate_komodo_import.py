#!/usr/bin/env python3
"""
Generate a Komodo TOML import file from all docker-compose examples
"""

import os
from pathlib import Path

def escape_triple_quotes(content):
    """Escape triple quotes in docker-compose content to prevent TOML parsing issues"""
    return content.replace('"""', '\\"\\"\\"')

def generate_toml():
    examples_dir = Path("examples")
    output_lines = []

    # Find all docker-compose files
    compose_files = sorted(examples_dir.glob("*/docker-compose.yml"))

    for compose_file in compose_files:
        stack_name = compose_file.parent.name

        # Read the docker-compose content
        try:
            with open(compose_file, 'r') as f:
                file_contents = f.read()

            # Escape triple quotes if present
            file_contents = escape_triple_quotes(file_contents)

            # Generate TOML entry
            output_lines.append('[[stack]]')
            output_lines.append(f'name = "{stack_name}"')
            output_lines.append('[stack.config]')
            output_lines.append('server = "Local"')
            output_lines.append('file_contents = """')
            output_lines.append(file_contents)
            output_lines.append('"""')
            output_lines.append('')
            output_lines.append('##')
            output_lines.append('')

            print(f"Added: {stack_name}")

        except Exception as e:
            print(f"Error processing {compose_file}: {e}")
            continue

    # Write to output file
    output_file = "komodo_stacks_import.toml"
    with open(output_file, 'w') as f:
        f.write('\n'.join(output_lines))

    print(f"\n✓ Generated {output_file} with {len(compose_files)} stacks")

if __name__ == "__main__":
    generate_toml()
