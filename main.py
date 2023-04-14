class Person:
    # 初期設定
    # selfはthisみたいなもの、必ず入れる。
    # 名前,国籍,年齢
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age

    def __call__(self, name):
        print(f"{name}さん、こんにちは。私は{self.name}です。")
        print("call関数から呼び出されました。")
    # 関数の形はメソッド
    # 何も入れなくてもselfは必ず入れる
    def say_hello(self, name):
        print(f"{name}さん、こんにちは。私は{self.name}です。")

imanishi = Person(name = "今西", nationality="日本", age = 26)

mike = Person(name="マイク", nationality="アメリカ", age=23)

# 今西の年齢と国籍を表示
print(imanishi.age)
print(imanishi.nationality)
# マイクの年齢を表示
print(mike.age)

imanishi.say_hello(name="佐藤")
mike.say_hello("鈴木")

# call関数はインスタンス名()で呼び出す事が出来る。
imanishi(name="佐藤")
# imanishi.__call__(name="佐藤")
