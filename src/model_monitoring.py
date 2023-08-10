import argparse
import pandas as pd


import datetime
from evidently.metrics import ColumnDriftMetric
from evidently.metrics import ColumnSummaryMetric
from evidently.metrics import DatasetDriftMetric
from evidently.metrics import DatasetMissingValuesMetric
from evidently.report import Report
from evidently.test_preset import DataDriftTestPreset
from evidently.test_suite import TestSuite
from evidently.ui.workspace import Workspace
from evidently.ui.workspace import WorkspaceBase
from src.get_data import read_params


def create_project(workspace: WorkspaceBase, project_name, project_desc):

    project = workspace.create_project(project_name)

    project.description = project_desc

    return project


def create_report(i: int, ref, cur):
    data_drift_report = Report(
        metrics=[
            DatasetDriftMetric(),
            DatasetMissingValuesMetric(),
            ColumnDriftMetric(column_name="Feature_1", stattest="wasserstein"),
            ColumnSummaryMetric(column_name="Feature_1"),
            ColumnDriftMetric(column_name="Feature_2", stattest="wasserstein"),
            ColumnSummaryMetric(column_name="Feature_2"),
        ],
        timestamp=datetime.datetime.now() + datetime.timedelta(days=i),
    )

    data_drift_report.run(reference_data=ref,
                          current_data=cur.iloc[100 * i: 100 * (i + 1), :])
    return data_drift_report


def create_test_suite(i: int, ref, cur):
    data_drift_test_suite = TestSuite(
        tests=[DataDriftTestPreset()],
        timestamp=datetime.datetime.now() + datetime.timedelta(days=i),
    )

    data_drift_test_suite.run(
        reference_data=ref, current_data=cur.iloc[100 * i: 100 * (i + 1), :])
    return data_drift_test_suite


def model_monitoring(config_path):
    config = read_params(config_path)

    train_data_path = config["split_data"]["train_path"]
    new_train_data_path = config["split_data"]["test_path"]

    project_name = config["evidently"]["project_name"]
    project_desc = config["evidently"]["project_desc"]

    workspace = config["evidently"]["workspace"]

    ref = pd.read_csv(train_data_path)
    cur = pd.read_csv(new_train_data_path)

    ws = Workspace.create(workspace)
    project = create_project(ws, project_name, project_desc)
    print(project)

    for i in range(0, 5):
        report = create_report(i=i, ref=ref, cur=cur)
        ws.add_report(project.id, report)

        test_suite = create_test_suite(i=i, ref=ref, cur=cur)
        ws.add_test_suite(project.id, test_suite)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    model_monitoring(config_path=parsed_args.config)
