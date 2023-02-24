import 'dart:math';
import 'Dart:io' as io;

//inputはボタンなどの入力、printはTextなどの出力に読み替えて

void main() {
  kazuate();
}
String input(){
return io.stdin.readLineSync();
}

//数あてゲーム
void kazuate(){
  int _num = 5;//仮置き
  var _masslist = new List.generate(_num, (i)=> i+1);
  _masslist.shuffle();
  List _pastcomparison = <List>[];
  for(int i = 0; i < 7; i++){
    var _line1 = input();
    int a = _masslist.indexOf(int.parse(_line1));
    var _line2 = input();
    int b = _masslist.indexOf(int.parse(_line2));
    _pastcomparison.add([a, b]);//後の関数で比較結果を表示したい
    if(a < b){
      print("$_line1は$_line2より軽いです。");
    }
    else{
      print("$_line1は$_line2より重いです。");
    }
  };
  List _ansnum = <int>[input()];
  if (_ansnum == _masslist){
    print("正解！");
  }
  else{
    print("不正解");
    print("正解は軽い方から順に$_ansnumです。");
  }

  void _incrementCounter() {//初期設定で球の数を選択(増加)
    setState(() {
      _num++;
    });
            Text(
              '$_num',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
  },
  void _incrementCounter() {//初期設定で球の数を選択(減少)
    setState(() {
      _num--;
    });
  }
}
            Text(
              '$_num',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
  },

  floatingActionButton: FloatingActionButton(
          onPressed: _whetherheavy,
          tooltip: 'Increment',
          child: const Icon(Icons.add),
  ),
  
  floatingActionButton: FloatingActionButton(
          onPressed: _incrementCounter,
          tooltip: 'Increment',
          child: const Icon(Icons.exposure_plus_1),
  ),
  floatingActionButton: FloatingActionButton(
          onPressed: _DecrementCounter,
          tooltip: 'Decrement',
          child: const Icon(Icons.exposure_minus_1),
  ),
//ひっかけ和差算
            Text(
              '鉛筆と消しゴムを1つずつ買うと合計$_sum円です。鉛筆は消しゴムより$_diff円高いです。消しゴムはいくらでしょう。',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
  },

//石取りゲーム
void ishitori(){
  List _stonelist = new List.generate(50, (i)=> i+1);
  _stonelist.shuffle();
  int _stone = _stonelist[0];
  List _maxlist = new List.generate(8, (i)=> i+1);
  _maxlist.shuffle();
  int _max = _maxlist[0];
  bool _turn = true;
  int _yourstone = 0;//なぜかこれ入れないとエラー出る
  int _mystone = 0;//これも
  while (_stone > 0){
    if (_turn){//使用者の番
      int _yourstone = int.parse(input());
      if (_stone < _yourstone){
        print("場の石の数より多い数の石は取れません。");
      }
      else if (_max > _yourstone){
        print("$_max個を超える石は取り除けません。");
      }
      else{
        _stone -= _yourstone;
        print("あなたは$_yourstone個の石を取り除きました。");
      }
    }
    else{//CPUの番
      if (_stone <= _max){
        int _mystone = _stone;
        _stone -= _mystone;
      }
      else{
        int _mystone = _max + 1 - _yourstone;
        _stone -= _mystone;
      }
      print("相手は$_mystone個の石を取り除きました。");
      _turn = false;
    };
  };
}

            Text(//出題
              'ここに石が$_stone個あります。あなたと太郎さんはこれから石取りゲームをします。各ターン、1個以上$_max個以下の石を取り除き、先に取り除けなくなった方が負けです。',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
  },

            Text(
              'いくつ取り除きますか？',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
  },