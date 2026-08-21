import os
import hashlib
import subprocess


class SonarDemo:

    # Security Hotspot: Hardcoded credential
    PASSWORD = "Admin123"

    def sql_injection(self, user_input):
        # Vulnerability: SQL Injection pattern
        query = "SELECT * FROM users WHERE id = '" + user_input + "'"
        print(query)

    def command_injection(self, cmd):
        # Vulnerability: Command Injection
        os.system(cmd)

    def weak_hash(self, password):
        # Security Hotspot: Weak hashing algorithm
        return hashlib.md5(password.encode()).hexdigest()

    def bug_null_reference(self):
        # Bug: None access
        value = None
        return value.upper()

    def unused_variable(self):
        # Code Smell
        x = 100
        y = 200
        return 10

    def duplicated_code_1(self):
        total = 0

        for i in range(10):
            total += i

        if total > 10:
            print("Large")

        return total

    def duplicated_code_2(self):
        total = 0

        for i in range(10):
            total += i

        if total > 10:
            print("Large")

        return total

    def long_method(self):
        # Code Smell: Excessively long method
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6
        g = 7
        h = 8
        i = 9
        j = 10
        k = 11
        l = 12
        m = 13
        n = 14
        o = 15

        result = (
            a+b+c+d+e+f+g+h+i+j+k+l+m+n+o
        )

        print(result)

    def empty_exception(self):
        try:
            x = 10 / 0
        except Exception:
            pass

    def shell_call(self):
        # Security concern
        subprocess.call("ls -la", shell=True)

    def always_true(self):
        # Code Smell
        if True:
            print("Always true")

    def unreachable_code(self):
        return
        print("This line is unreachable")


if __name__ == "__main__":
    app = SonarDemo()

    app.sql_injection("1 OR 1=1")
    app.command_injection("echo hello")
    app.weak_hash("secret")
    app.unused_variable()
    app.duplicated_code_1()
    app.duplicated_code_2()
    app.long_method()
    app.empty_exception()
    app.shell_call()
    app.always_true()
