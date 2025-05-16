## Buggy code
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
		return new JDBCHeatbeat();
	}

	@Override
	public void createNewConnection(ResponseHandler handler,String schema) throws IOException {
		DBHostConfig dsc = getConfig();
		JDBCConnection c = new JDBCConnection();

		c.setHost(dsc.getIp());
		c.setPort(dsc.getPort());
		c.setPool(this);
		try {
			Connection con = DriverManager.getConnection(dsc.getUrl(),
					dsc.getUser(), dsc.getPassword());
			// c.setIdleTimeout(pool.getConfig().getIdleTimeout());
			c.setCon(con);
			// notify handler
			handler.connectionAcquired(c);
		} catch (Exception e) {
			handler.connectionError(e, c);
		}

	}

}

```

## Error
解决了连接JDBC的出现空指针的小bug

## Error Description
-connect error JDBCConnection [autocommit=true, txIsolation=0, running=false, borrowed=true, id=0, host=localhost, port=3306]java.lang.NullPointerException

