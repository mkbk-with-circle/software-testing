Based on the error description, the issue occurs when trying to get the user role before the nickname is stored in multiUserChat. The fix is to handle the case when the nickname is null by returning a guest role in the `getUserRole()` method. Here's the fixed code:

```java
public ChatRoomMemberRole getUserRole()
{
    if(this.role == null)
    {
        Resourcepart nickname = multiUserChat.getNickname();
        if (nickname == null)
            return ChatRoomMemberRole.GUEST;
            
        Occupant o = multiUserChat.getOccupant(JidCreate.entityFullFrom(
            multiUserChat.getRoom(), nickname));

        if(o == null)
            return ChatRoomMemberRole.GUEST;
        else
            this.role = smackRoleToScRole(o.getRole(), o.getAffiliation());
    }

    return this.role;
}
```

The fix adds a null check for the nickname before trying to create the JID. If the nickname is null, it returns the GUEST role. This prevents the IllegalArgumentException when the Resourcepart is null.

The rest of the code remains unchanged. This change ensures that when we receive presence and dispatch the user role before the nickname is stored, we gracefully handle the case by returning a guest role rather than throwing an exception.