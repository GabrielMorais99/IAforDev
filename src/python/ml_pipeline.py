from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_pipeline(frame: pd.DataFrame, target: str) -> Pipeline:
    features = frame.drop(columns=[target])
    numeric = features.select_dtypes(include="number").columns.tolist()
    categorical = [column for column in features.columns if column not in numeric]

    preprocessing = ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                numeric,
            ),
            (
                "categorical",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical,
            ),
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            ("model", LogisticRegression(max_iter=1_000, class_weight="balanced")),
        ]
    )


def train(dataset: Path, target: str, output_dir: Path) -> None:
    frame = pd.read_csv(dataset)
    if target not in frame.columns:
        raise ValueError(f"Target '{target}' não encontrado. Colunas: {frame.columns.tolist()}")
    if frame[target].nunique() < 2:
        raise ValueError("O target precisa possuir pelo menos duas classes.")

    x = frame.drop(columns=[target])
    y = frame[target]
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    pipeline = build_pipeline(frame, target)
    pipeline.fit(x_train, y_train)
    predictions = pipeline.predict(x_test)
    report = classification_report(y_test, predictions, output_dict=True, zero_division=0)

    output_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, output_dir / "model.joblib")
    (output_dir / "metrics.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Baseline reproduzível de classificação.")
    parser.add_argument("dataset", type=Path, help="CSV de entrada")
    parser.add_argument("--target", required=True, help="Coluna alvo")
    parser.add_argument("--output", type=Path, default=Path("artifacts"))
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    train(args.dataset, args.target, args.output)
