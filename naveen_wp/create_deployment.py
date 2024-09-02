from prefect import flow
# Source for the code to deploy (here, a GitHub repo)
SOURCE_REPO="https://github.com/NAVEENKANUGANTI/prefect_pratice_new.git"

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/NAVEENKANUGANTI/prefect_pratice_new.git",
        entrypoint="my_gh_workflow:repo_infocd",
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool",
        cron="0 1 * * *",
    )