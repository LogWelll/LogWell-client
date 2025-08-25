from logwell_client.client import SyncLogClient, AsyncLogClient
import asyncio

# # instanciate the sync client
# client = SyncLogClient(
#     base_url="http://localhost:8000/",
#     api_key="key1",
# )

# read list
# log_list = client.read_log(
#     query={
#         "list": True,
#     }
# )

# print(
#     log_list.json()
# )

# read by uid
# log = client.read_log(
#     query={
#         "uid": "a02c1d7a-e5ac-4194-b957-47cd4410aec0",
#     }
# )

# print(log.json())

# read by tag
# tag_logs = client.read_log(
#     query={
#         "tag": "tag1",
#     }
# )

# print(
#     tag_logs.json()
# )

# read by level
# level_logs = client.read_log(
#     query={
#         "level": "INFO",
#     }
# )

# print(
#     level_logs.json()
# )

# read by group path exact_only
# group_path_logs = client.read_log(
#     query={
#         "group_path": "section",
#         "group_path_flag": "exact_only",
#     }
# )

# print(
#     group_path_logs.json()
# )

# read by group path all children
# group_path_logs = client.read_log(
#     query={
#         "group_path": "section",
#         "group_path_flag": "all_children",
#     }
# )

# print(
#     group_path_logs.json()
# )



AsyncLogClient = AsyncLogClient(
    base_url="http://localhost:8000/",
    api_key="key1"
)

async def main():
    # read list
    # log_list = await AsyncLogClient.read_log(
    #     query={
    #         "list": True,
    #     }
    # )

    # print(
    #     log_list.json()
    # )

    # read by uid
    # log = await AsyncLogClient.read_log(
    #     query={
    #         "uid": "a02c1d7a-e5ac-4194-b957-47cd4410aec0",
    #     }
    # )

    # print(log.json())

    # read by tag
    # tag_logs = await AsyncLogClient.read_log(
    #     query={
    #         "tag": "tag1",
    #     }
    # )

    # print(
    #     tag_logs.json()
    # )

    # read by level
    # level_logs = await AsyncLogClient.read_log(
    #     query={
    #         "level": "INFO",
    #     }
    # )

    # print(
    #     level_logs.json()
    # )

    # read by group path exact_only
    # group_path_logs = await AsyncLogClient.read_log(
    #     query={
    #         "group_path": "section",
    #         "group_path_flag": "exact_only",
    #     }
    # )

    # print(
    #     group_path_logs.json()
    # )

    # read by group path exact_only
    group_path_logs = await AsyncLogClient.read_log(
        query={
            "group_path": "section",
            "group_path_flag": "exact_only",
        }
    )

    print(
        group_path_logs.json()
    )

    # read by group path all children
    # group_path_logs = await AsyncLogClient.read_log(
    #     query={
    #         "group_path": "section",
    #         "group_path_flag": "all_children",
    #     }
    # )

    # print(
    #     group_path_logs.json()
    # )

    await AsyncLogClient.aclose()


asyncio.run(main())