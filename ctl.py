import cmd
import os
import readline


RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
CYAN = "\033[96m"

PROMPT_START_IGNORE = "\001"
PROMPT_END_IGNORE = "\002"


def input_swallowing_interrupt(_input):
    def _input_swallowing_interrupt(*args):
        try:
            return _input(*args)
        except KeyboardInterrupt:
            print("^C")
            return "\n"

    return _input_swallowing_interrupt


class ComputorShell(cmd.Cmd):
    prompt = f"{PROMPT_START_IGNORE}{BOLD}{CYAN}{PROMPT_END_IGNORE}computorv2>{PROMPT_START_IGNORE}{RESET}{PROMPT_END_IGNORE} "

    def cmdloop(self, *args, **kwargs):
        old_input_fn = cmd.__builtins__["input"]
        cmd.__builtins__["input"] = input_swallowing_interrupt(old_input_fn)
        try:
            super().cmdloop(*args, **kwargs)
        finally:
            cmd.__builtins__["input"] = old_input_fn

        self.old_completer = readline.get_completer()
        readline.set_completer(self.complete)
        readline.parse_and_bind(self.completekey + ": complete")
        old_delims = readline.get_completer_delims()
        readline.set_completer_delims(old_delims.replace("-", ""))

    def default(self, arg):
        if arg == "EOF":
            print()
            return True
        else:
            print(f"{arg.split()[0]}: command not found")

    def do_exit(self, _):
        """exit : exit the taskmaster shell"""
        return True

    # TODO: remove
    def do_ooga(self, arg):
        """ooga : chaka"""
        print(arg + " yourself" if arg else "chaka")


if __name__ == "__main__":
    INTRO_CHAR = "="
    width = os.get_terminal_size().columns
    top_line = INTRO_CHAR * width
    middle_line = "  WELCOME TO COMPUTORV2  ".center(width, INTRO_CHAR)
    intro = f"{BOLD}{GREEN}{top_line}\n{middle_line}\n{top_line}{RESET}"
    ComputorShell().cmdloop(intro)
    print("Goodbye.")
