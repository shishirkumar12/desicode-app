def run_desicode(code, external_vars=None):
    output = []
    variables = external_vars if external_vars is not None else {}
    functions = {}
    lines = code.strip().split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # 🗣️ Print
        if line.startswith("bol "):
            value = line[4:].strip()
            if value.startswith('"') and value.endswith('"'):
                output.append(value[1:-1])
            elif value in variables:
                output.append(str(variables[value]))
            else:
                output.append(f"Error: '{value}' not found")

        # 📦 Variable
        elif line.startswith("rakh "):
            parts = line.split(" ", 2)
            if len(parts) == 3:
                var, val = parts[1], parts[2].strip('"')
                if val.replace('.', '', 1).isdigit():
                    val = float(val)
                    val = int(val) if val.is_integer() else val
                variables[var] = val
            else:
                output.append("Syntax Error in 'rakh'.")

        # 🔁 Loop
        elif line.startswith("repeat "):
            parts = line.split(" ", 2)
            if len(parts) == 3 and parts[1].isdigit():
                count = int(parts[1])
                for _ in range(count):
                    inner = run_desicode(parts[2], variables)
                    output.append(inner)
            else:
                output.append("Syntax Error in 'repeat'.")

        # ❓ Condition
        elif line.startswith("agar "):
            if "barabar" in line and "toh" in line:
                try:
                    cond, action = line.split("toh", 1)
                    _, var, _, val = cond.strip().split()
                    val = val.strip('"')
                    if str(variables.get(var, "")) == val:
                        inner = run_desicode(action.strip(), variables)
                        output.append(inner)
                except:
                    output.append("Syntax Error in 'agar'.")

        # ➕➖✖️➗ Math operations
        elif any(line.startswith(op) for op in ["jod", "ghata", "guna", "bhaag"]):
            cmd, a, b = line.split()
            try:
                a, b = float(a), float(b)
                if cmd == "jod": result = a + b
                elif cmd == "ghata": result = a - b
                elif cmd == "guna": result = a * b
                elif cmd == "bhaag":
                    result = a / b if b != 0 else "Math Error: Zero se bhaag nahi hota."
                if isinstance(result, float) and not isinstance(result, str):
                    result = int(result) if result.is_integer() else result
                output.append(str(result))
            except:
                output.append(f"Syntax Error in '{cmd}'.")

        # 🧑‍💻 Input
        elif line.startswith("pucho "):
            var = line.split()[1]
            val = input(f"{var}: ")
            variables[var] = val

        # 🧱 Function definition
        elif line.startswith("kaam karle "):
            func_name = line.split(" ")[2]
            func_body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("khatam"):
                func_body.append(lines[i])
                i += 1
            functions[func_name] = '\n'.join(func_body)

        # 🔁 Function call
        elif line in functions:
            result = run_desicode(functions[line], variables)
            output.append(result)

        else:
            output.append("Unknown command: " + line)

        i += 1

    return "\n".join([o for o in output if o])



