# API列表

## 台网列表

**Resources URI**

```
/v1/basic/networks/[?page=:num]
```

**Example:**

```
GET /v1/basic/networks/
```

**Status:**

```
200 OK
```

**Requests Properities**

| Property | Description | require            | Type | Default |
| -------- | ------------| ---------------- | ---- | ------- |
| page     | 当前页面     | False             | int  | 1       |

**Resources Properties:**

| Property | Description      | Type | Default |
| -------- | ---------------- | ---- | ------- |
| network       | 台网实体(见[台网条目](#network)) | str  | -       |
| count    | 总数             | int  | 0       |
| next     | 下一页 url  | str | null |
| previous | 上一页url | str | null |
| page | 当前页面 | int | 1 |

## 添加台网条目

**Resources URI**

```
/v1/basic/networks/
```

**Example:**

```
POST /v1/basic/networks/
```

**Status:**

```
201 Created
```

**Requests Properities**

| Property | Description| require | Type | Default |
| -------- | ----------- | ------ | ---- | ------- |
| code     | 台网代码     | True | str  | -       |
| name     | 台网名称     | False  | str  | ''      |
| remark   | 台网描述信息  | False | str  | ''      |

## <span id="network">台网条目</span>


**Resources URI**

```
/v1/basic/networks/:id/
```

**Example:**

```
GET /v1/basic/networks/1/
```

**Status:**

```
200 OK
```

**Resources Properties:**

| Property | Description  | Type | Default |
| -------- | ------------ | ---- | ------- |
| id       | 台网id       | str  | -       |
| code     | 台网代码     | str  | -       |
| name     | 台网名称     | str  | ''      |
| created  | 创建时间     | str  | ''      |
| updated  | 更新时间     | str  | ''      |
| remark   | 台网描述信息 | str  | ''      |

- /basic/networks/

  - get 

    ```json
    # 获得 network 列表
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "code": "G1",
                "name": "",
                "slug": "g1",
                "created": "2020-02-03T08:57:01.192533Z",
                "updated": "2020-02-03T08:57:01.192626Z",
                "remark": ""
            },
            {
                "id": 2,
                "code": "YSW",
                "name": "亚失稳",
                "slug": "ysw",
                "created": "2020-02-06T16:23:55.980706Z",
                "updated": "2020-02-06T16:23:55.980748Z",
                "remark": ""
            }
        ]
    }
    ```

  - post

    

    

- /basic/networks/<int:id>

- /basic/networks/

- /basic/networks/<int:network_id>/stations/

- /basic/networks/

