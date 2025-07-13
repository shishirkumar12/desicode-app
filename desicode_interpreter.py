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
                output.append(value[1:-1].encode().decode('unicode_escape'))
            elif value in variables:
                output.append(str(variables[value]))
            else:
                output.append(f"Error: '{value}' not found")

        # 📦 Variable assignment (rakh a = 10) or expression (rakh c jod a b)
        elif line.startswith("rakh "):
            parts = line.split()
            # Case: rakh a = 10
            if len(parts) == 4 and parts[2] == "=":
                var = parts[1]
                val = parts[3].strip('"')
                if val.replace('.', '', 1).isdigit():
                    val = float(val)
                    val = int(val) if val.is_integer() else val
                variables[var] = val

            # Case: rakh a 10
            elif len(parts) == 3:
                var, val = parts[1], parts[2].strip('"')
                if val.replace('.', '', 1).isdigit():
                    val = float(val)
                    val = int(val) if val.is_integer() else val
                variables[var] = val

            # Case: rakh c jod a b
            elif len(parts) == 5 and parts[2] in ["jod", "ghata", "guna", "bhaag"]:
                var, op, a, b = parts[1], parts[2], parts[3], parts[4]
                try:
                    a_val = float(variables.get(a, a))
                    b_val = float(variables.get(b, b))
                    if op == "jod":
                        result = a_val + b_val
                    elif op == "ghata":
                        result = a_val - b_val
                    elif op == "guna":
                        result = a_val * b_val
                    elif op == "bhaag":
                        result = a_val / b_val if b_val != 0 else "Math Error: Zero se bhaag nahi hota."
                    if isinstance(result, float) and not isinstance(result, str):
                        result = int(result) if result.is_integer() else result
                    variables[var] = result
                except:
                    output.append(f"Math error in '{op}' expression.")
            else:
                output.append("Syntax Error in 'rakh'.")

        # 🔁 Repeat
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
        elif line.startswith("agar ") and "barabar" in line and "toh" in line:
            try:
                cond, action = line.split("toh", 1)
                _, var, _, val = cond.strip().split()
                val = val.strip('"')
                if str(variables.get(var, "")) == val:
                    inner = run_desicode(action.strip(), variables)
                    output.append(inner)
            except:
                output.append("Syntax Error in 'agar'.")

        # ➕➖✖️➗ Direct math (print only)
        elif any(line.startswith(op) for op in ["jod", "ghata", "guna", "bhaag"]):
            parts = line.split()
            if len(parts) == 3:
                cmd, a, b = parts
                try:
                    a_val = float(variables.get(a, a))
                    b_val = float(variables.get(b, b))
                    if cmd == "jod":
                        result = a_val + b_val
                    elif cmd == "ghata":
                        result = a_val - b_val
                    elif cmd == "guna":
                        result = a_val * b_val
                    elif cmd == "bhaag":
                        result = a_val / b_val if b_val != 0 else "Math Error: Zero se bhaag nahi hota."
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

    return '\n'.join([o for o in output if o])




