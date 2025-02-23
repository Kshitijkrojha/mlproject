import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import customexception
from src.logger import logging

from src.utils import save_object,evaluate_model

@dataclass
class ModelTrainerConfig:
    Trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Initiating model training")
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "RandomForest": RandomForestRegressor(),
                "GradientBoosting": GradientBoostingRegressor(),
                "AdaBoost": AdaBoostRegressor(),
                "XGBoost": XGBRegressor(),
                "KNeighbours": KNeighborsRegressor(),
                "DecisionTree": DecisionTreeRegressor(),
                "LinearRegression": LinearRegression(),
            }

            model_report: dict = evaluate_model(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test, models=models)

            logging.info(f"Model Report: {model_report}")

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            logging.info(f"Best Model Found: {best_model_name} with score: {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.Trained_model_file_path,
                obj=best_model
            )

            return best_model_score

        except Exception as e:
            logging.error("Error in model training")
            raise customexception(e, sys)