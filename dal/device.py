from pydal import DAL, Field

db = DAL('postgres://postgres:123456@localhost:5432/sentinel')

db.define_table('device',
                Field('name', 'string', length=128, required=True),
                Field('description', 'string', length=256),
                Field('address', 'string', length=128),
                Field('os_type', 'string', length=128),
                Field('last_scan_date', 'datetime'),
                migrate=False
                )
