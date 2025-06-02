修复后的代码如下，主要修复了JDBCHeartbeat类名拼写错误和可能的空指针问题：

```java
package org.opencloudb.jdbc;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;

import org.opencloudb.backend.PhysicalDatasource;
import org.opencloudb.config.model.DBHostConfig;
import org.opencloudb.config.model.DataHostConfig;
import org.opencloudb.heartbeat.DBHeartbeat;
import org.opencloudb.mysql.nio.handler.ResponseHandler;

public class JDBCDatasource extends PhysicalDatasource {
    public JDBCDatasource(DBHostConfig config, DataHostConfig hostConfig,
            boolean isReadNode) {
        super(config, hostConfig, isReadNode);
    }

    @Override
    public DBHeartbeat createHeartBeat() {
        return new JDBCHeartbeat();
    }

    @Override
    public void createNewConnection(ResponseHandler handler, String schema) throws IOException {
        DBHostConfig dsc = getConfig();
        if (dsc == null) {
            throw new IOException("DBHostConfig is null");
        }

        JDBCConnection c = new JDBCConnection();
        c.setHost(dsc.getIp());
        c.setPort(dsc.getPort());
        c.setPool(this);
        
        try {
            Connection con = DriverManager.getConnection(
                dsc.getUrl() != null ? dsc.getUrl() : "",
                dsc.getUser() != null ? dsc.getUser() : "",
                dsc.getPassword() != null ? dsc.getPassword() : "");
            c.setCon(con);
            handler.connectionAcquired(c);
        } catch (Exception e) {
            handler.connectionError(e, c);
        }
    }
}
```

主要修改：
1. 修正了类名拼写错误，将`JDBCHeatbeat`改为`JDBCHeartbeat`
2. 添加了对DBHostConfig为空时的检查
3. 对连接参数(url, user, password)进行了空值检查
4. 改进了异常处理，确保在配置错误时能抛出有意义的异常