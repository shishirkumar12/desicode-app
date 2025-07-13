def run_desicode(code):
    output = []
    variables = {}
    lines = code.strip().split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Skip empty lines
        if not line:
            i += 1
            continue

        # 🗣️ Print command
        if line.startswith("bol "):
            value = line[4:].strip()
            if value.startswith('"') and value.endswith('"'):
                output.append(value[1:-1])
            elif value in variables:
                output.append(str(variables[value]))
            else:
                output.append(f"Error: '{value}' not found")

        # 📦 Variable assignment
        elif line.startswith("rakh "):
            parts = line.split(" ", 2)
            if len(parts) == 3:
                var_name = parts[1]
                var_value = parts[2].strip('"')
                # Try to convert to number if possible
                if var_value.isdigit():
                    var_value = int(var_value)
                variables[var_name] = var_value
            else:
                output.append("Syntax Error in 'rakh' command.")

        # 🔁 Repeat loop
        elif line.startswith("repeat "):
            parts = line.split(" ", 2)
            if len(parts) == 3:
                count_str, cmd = parts[1], parts[2]
                if count_str.isdigit():
                    count = int(count_str)
                    for _ in range(count):
                        inner_result = run_desicode(cmd)
                        output.append(inner_result)
                else:
                    output.append("Error: repeat count must be a number.")
            else:
                output.append("Syntax Error in 'repeat'.")

        # ❓ Conditionals
        elif line.startswith("agar "):
            if "barabar" in line and "toh" in line:
                try:
                    condition_part, command_part = line.split("toh", 1)
                    _, var_name, _, expected_value = condition_part.strip().split()
                    expected_value = expected_value.strip('"')
                    actual_value = str(variables.get(var_name, ""))
                    if actual_value == expected_value:
                        result = run_desicode(command_part.strip())
                        output.append(result)
                except:
                    output.append("Syntax Error in 'agar' condition.")
            else:
                output.append("Syntax Error in 'agar' statement.")

        else:
            output.append(f"Unknown command: {line}")

        i += 1

    return "\n".join(output)

