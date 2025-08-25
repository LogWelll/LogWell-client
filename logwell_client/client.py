from .schema import GroupPathFlag, LogCreateSchema, Endpoint, LogQuerySchema
import httpx


class SyncLogClient:
    def __init__(self, base_url: str, api_key: str, tenant: str | None = None):
        self.tenant = tenant
        self.client = httpx.Client(base_url=base_url, headers={"x-API-key": api_key})

    def create_log(
        self, log: LogCreateSchema | dict, endpoint: Endpoint = Endpoint.Blocking
    ) -> dict:
        if self.tenant:
            if isinstance(log, LogCreateSchema):
                log.tenant = self.tenant
            else:
                log["tenant"] = self.tenant

        response = self.client.post(
            endpoint, json=log.model_dump() if isinstance(log, LogCreateSchema) else log
        )
        return response

    def close(self):
        self.client.close()


    def read_log(
        self, query: LogQuerySchema | dict
    ):
        if isinstance(query, dict):
            query = LogQuerySchema(**query)
        
        if query.list:
            response = self.client.get(Endpoint.List, params=query.query_params.model_dump() if query.query_params else None)
        elif query.uid:
            response = self.client.get(Endpoint.Uid + query.uid)
        elif query.tag:
            response = self.client.get(Endpoint.Tag + query.tag, params=query.query_params.model_dump() if query.query_params else None)
        elif query.level:
            response = self.client.get(Endpoint.Level + query.level.value, params=query.query_params.model_dump() if query.query_params else None)
        elif query.group_path:
            if query.group_path_flag == GroupPathFlag.ExactOnly:
                response = self.client.get(Endpoint.Group_path + query.group_path + '/', params=query.model_dump() if query.query_params else None)
            else:
                response = self.client.get(Endpoint.Group_path + query.group_path + '/' + 'children' + '/', params=query.model_dump() if query.query_params else None)

        if response.status_code == 200:
            return response
        
        response.raise_for_status()


class AsyncLogClient:
    def __init__(self, base_url: str, api_key: str, tenant: str | None = None):
        self.tenant = tenant
        self.client = httpx.AsyncClient(
            base_url=base_url, headers={"x-API-key": api_key}
        )

    async def create_log(
        self, log: LogCreateSchema | dict, endpoint: Endpoint = Endpoint.Blocking
    ) -> dict:
        if self.tenant:
            if isinstance(log, LogCreateSchema):
                log.tenant = self.tenant
            else:
                log["tenant"] = self.tenant

        response = await self.client.post(
            endpoint, json=log.model_dump() if isinstance(log, LogCreateSchema) else log
        )
        return response

    async def read_log(
        self, query: LogQuerySchema | dict
    ):
        if isinstance(query, dict):
            query = LogQuerySchema(**query)
    
        if query.list:
            response = await self.client.get(Endpoint.List, params=query.query_params.model_dump() if query.query_params else None)
        elif query.uid:
            response = await self.client.get(Endpoint.Uid + query.uid)
        elif query.tag:
            response = await self.client.get(Endpoint.Tag + query.tag, params=query.query_params.model_dump() if query.query_params else None)
        elif query.level:
            response = await self.client.get(Endpoint.Level + query.level.value, params=query.query_params.model_dump() if query.query_params else None)
        elif query.group_path:
            if query.group_path_flag == GroupPathFlag.ExactOnly:
                response = await self.client.get(Endpoint.Group_path + query.group_path + '/', params=query.model_dump() if query.query_params else None)
            else:
                response = await self.client.get(Endpoint.Group_path + query.group_path + '/' + 'children' + '/', params=query.model_dump() if query.query_params else None)

        if response.status_code == 200:
            return response
        
        response.raise_for_status()

    async def aclose(self):
        await self.client.aclose()
