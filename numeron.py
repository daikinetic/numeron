# 使用言語は Python です
# *Google Colablatory で作成したコードなので、以下それに応じたコメントを付与しています

# 3桁の連番を当てる推測ゲームです
# セル上で「Shift + Enter」を押すとコードが実行されます

# ヌメロン　N回試行
# 〈1〉&〈2〉
import random
print('数当てゲームを始めます。3桁の数を当ててください！（半角数字で入力してください）（3桁の数字は重複組み合わせも考慮してください）')
answer = list()
for n in range(3):
  answer.append(random.randint(0,9))

# 〈3〉
prediction = list()
for n in range(3):
  data = int(input('{}桁目の予想を入力(0~9)>>'.format(n+1)))
  prediction.append(data)

# 〈4〉
count_eat = 0
count_bite = 0
for a in prediction:
  count = 0
  for b in answer:
    if a == b:
      if prediction[count] == answer[count]:
        count_eat += 1
      else:
        count_bite += 1
    count += 1
print('{}EAT!{}BITE!'.format(count_eat,count_bite))

# 〈5〉
if count_eat == 3:
  print('正解です！')
  print('ゲームを終了します。お疲れ様でした！！')

# 〈6〉
else:
  key = int(input('続けますか？ 1:続ける 2:終了>>'))
  if key == 2:
    print('正解は{}{}{}でした！'.format(answer[0],answer[1],answer[2]))
    print('ゲームを終了します。お疲れ様でした！！')
  elif key == 1:
    print('ゲームを続行します')

# 〈7〉リストの要素変更：変数名[添え字]＝値
    isTrue = True
    while isTrue == True:
      for n in range(3):
        data = int(input('{}桁目の予想を入力(0~9)>>'.format(n+1)))
        prediction[n] = data
      count_eat = 0
      count_bite = 0
      for a in prediction:
        count = 0
        for b in answer:
          if a == b:
            if prediction[count] == answer[count]:
              count_eat += 1
            else:
              count_bite += 1
          count += 1
      print('{}EAT!{}BITE!'.format(count_eat,count_bite))

      if count_eat == 3:
        print('正解です！')
        break
      else:
        key = int(input('続けますか？ 1:続ける 2:終了>>'))
        if key == 2:
          print('正解は{}{}{}でした！'.format(answer[0],answer[1],answer[2]))
          isTrue = False

    print('ゲームを終了します。お疲れ様でした！！')
