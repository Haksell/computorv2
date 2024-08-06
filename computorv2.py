import cmd
import os


RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
CYAN = "\033[96m"

PROMPT_START_IGNORE = "\001"
PROMPT_END_IGNORE = "\002"


class ComputorShell(cmd.Cmd):
    prompt = f"{PROMPT_START_IGNORE}{BOLD}{CYAN}{PROMPT_END_IGNORE}computorv2>{PROMPT_START_IGNORE}{RESET}{PROMPT_END_IGNORE} "

    def __init__(self):
        super().__init__()
        self.variables = dict()

    def cmdloop(self, *args, **kwargs):
        def input_swallowing_interrupt(_input):
            def _input_swallowing_interrupt(*args):
                try:
                    return _input(*args)
                except KeyboardInterrupt:
                    print("^C")
                    return "\n"

            return _input_swallowing_interrupt

        old_input_fn = cmd.__builtins__["input"]
        cmd.__builtins__["input"] = input_swallowing_interrupt(old_input_fn)
        try:
            super().cmdloop(*args, **kwargs)
        finally:
            cmd.__builtins__["input"] = old_input_fn

    def do_exit(self, _):
        """exit : exit the program"""
        return True

    def do_vars(self, _):
        """vars : list all variables and their values"""
        if self.variables:
            for k, v in sorted(self.variables.items()):
                print(f"{k} = {v}")
        else:
            print("No variables in memory")

    def default(self, arg):
        if arg == "EOF":
            return True
        try:
            var_name, value = map(str.strip, arg.lower().split("=", 1))
            assert (
                all(map(str.isalpha, var_name))
                and len(var_name) >= 1
                and var_name != "i"
            )
            self.variables[var_name] = int(value)
        except (AssertionError, ValueError):
            print("Invalid command or assignment")


def main():
    INTRO_CHAR = "="
    width = os.get_terminal_size().columns
    top_line = INTRO_CHAR * width
    middle_line = "  WELCOME TO COMPUTORV2  ".center(width, INTRO_CHAR)
    intro = f"{BOLD}{GREEN}{top_line}\n{middle_line}\n{top_line}{RESET}"
    ComputorShell().cmdloop(intro)
    print("Goodbye.")


if __name__ == "__main__":
    main()
