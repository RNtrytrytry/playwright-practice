# Playwright(Python)によるE2Eテスト自動化の練習

練習用ECサイト「Sauce Demo」を題材に、Playwright + pytest でテスト自動化に取り組んだリポジトリです。

## 使用技術
- Python / pytest / Playwright
- GitHub Actions(更新のたびに自動実行)

## 構成
- `tests/` ではなく直下に `test_login.py`、`test_cart.py`
- `pages/`: 画面ごとの部品と操作をまとめたPage Object
- `conftest.py`: 「ログイン済み」の事前条件を作るfixture

## 動かし方
pip install -r requirements.txt
playwright install
pytest --headed

## 自動化の方針
### 自動化したもの
- ★ログイン(成功/パスワード誤り): 毎回確認が必要で、手順が固定のため
- ★カートへの追加: 購入フローの入口で、回帰の影響が大きいため

### あえて自動化していないもの
- ★画面の見た目・デザインの確認: 人の目で判断する部分で、自動化の費用対効果が低いため

### 工夫した点
- fixtureで事前条件を共通化し、重複を削減
- Page Objectで画面の変更に強い構成にした
- 失敗時にスクリーンショットを取得できる