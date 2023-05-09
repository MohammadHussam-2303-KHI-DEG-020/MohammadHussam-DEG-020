import fire
import mlflow
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def setup_rfc_pipeline(n):
    rfc = RandomForestClassifier(n_estimators=n)
    pipe = make_pipeline(SimpleImputer(strategy='mean'), StandardScaler(), rfc)
    return pipe
    

def split_data(df):
    X_df = df.iloc[:,1:12]
    y_df = df[["quality"]]

    
    x_train, x_test, y_train, y_test = train_test_split(X_df, y_df, test_size=0.2)
    return x_train, x_test, y_train, y_test


def track_with_mlflow(model, X_test, Y_test, mlflow, model_metadata):
    mlflow.log_params(model_metadata)
    mlflow.log_metric("accuracy", model.score(X_test, Y_test))
    mlflow.sklearn.log_model(model, "rfc", registered_model_name="sklearn_rfc")


def main(file_name: str, max_n: int):
    df = pd.read_csv(file_name)

    X_train, X_test, Y_train, Y_test = split_data(df)
    # let's check some other k
    n_list = range(95, max_n)

    for n in n_list:
        with mlflow.start_run():
            rfc_pipe = setup_rfc_pipeline(n)
            rfc_pipe.fit(X_train, Y_train)
            model_metadata = {"n": n}
            track_with_mlflow(rfc_pipe, X_test, Y_test, mlflow, model_metadata)

if __name__ == "__main__":
    fire.Fire(main)
