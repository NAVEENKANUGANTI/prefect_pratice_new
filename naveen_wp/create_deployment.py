from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/NAVEENKANUGANTI/prefect_pratice_new.git",
        entrypoint="my_gh_workflow.py:prefect_pratice_new",
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-managed-pool",
        cron="0 1 * * *",
    )