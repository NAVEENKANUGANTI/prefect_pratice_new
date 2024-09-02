from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/NAVEENKANUGANTI/prefect_pratice_new.git",
        entrypoint="my_gh_wf.py:repo_info",
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool",
        cron="0 1 * * *",
    )