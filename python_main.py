def main():
    greeting()

def greeting():
    print("Hello, World!")

if __name__ == "__main__":
    print(__name__) #__name__ は現在のモジュール名を保持する。モジュールとしてインポートされるとpython_mainとなる
    main()          # しかし、スクリプトが直接実行されているときには、__name__は__main__となる。
                    # つまり、このファイルがモジュールとして使われる場合には、このif文は成立しない