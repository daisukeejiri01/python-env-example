import unittest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tpot import TPOTClassifier

class TestIrisClassifier(unittest.TestCase):
    def setUp(self):
        # アヤメのデータセットをロード
        self.X, self.y = load_iris(return_X_y=True)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.3, random_state=42
        )
        # TPOT分類器のインスタンスを作成
        self.tpot = TPOTClassifier(
            generations=5, population_size=20, verbosity=0, random_state=42
        )

    def test_tpot_classifier(self):
        # モデルのトレーニング
        self.tpot.fit(self.X_train, self.y_train)
        # テストデータでのスコアを計算
        score = self.tpot.score(self.X_test, self.y_test)
        # スコアが一定の閾値を超えていることを確認
        self.assertGreater(score, 0.9)

if __name__ == '__main__':
    unittest.main()