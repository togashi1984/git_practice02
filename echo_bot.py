'''
あいさつアプリ

＃＃実行の流れ
1.実行すると「お名前は？」って出力される
2.ユーザーからの入力を受け付ける
3.「こんにちは〇〇さん」と出力する

'''
print('お名前は？')

name = input()
##nameに''はつけない
print('こんにちは、' + name + 'さん。')

name = input('お名前は？　')

print(f'こんにちは、{name}さん。')
