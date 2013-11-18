db.define_table('item',
                Field('name', 'string', default=None, required=True, requires=IS_NOT_EMPTY()), 
                format='%(name)s')