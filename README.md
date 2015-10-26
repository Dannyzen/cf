This is awesome

> ack-grep -A 5 --no-filename command_registry.CommandMetadata | ack-grep "Name":\ \ \|Description | grep -v Shortname | grep -v orgs | tr -d '[T(]' | tr -d ')' 
