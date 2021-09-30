class a:
    static='sathi'
    def change(self):
        self.static='babu'
print(a.static)
c=a()
c.change()
print(c.static)