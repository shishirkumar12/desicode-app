def run_desicode(code):
    output = []
    variables = {}
    lines = code.strip().split('\n')

    for line in lines:
        line = line.strip()

        if line.startswith("bol "):
            value = line[4:].strip()
            if value.startswith('"') and value.endswith('"'):
                output.append(value[1:-1])
            elif value in variables:
                output.append(str(variables[value]))
            else:
                output.append(f"Error: '{value}' not found")

        elif line.startswith("rakh "):
            parts = line.split(" ", 2)
            if len(parts) == 3:
                var_name = parts[1]
                var_value = parts[2].strip('"')
                variables[var_name] = var_value
            else:
                output.append("Syntax Error in 'rakh' command.")

        else:
            output.append("Unknown command: " + line)

    return "\n".join(output)
