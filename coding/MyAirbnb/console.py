import cmd

class myCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_hello(self, arg):
        print('hello', arg)


    def do_quit(self, arg):
        """Exits the program"""
        return True

if __name__ == '__main__':
    mycmd = myCommand()
    mycmd.cmdloop()