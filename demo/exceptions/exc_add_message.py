try:
    with open(path, "r") as f:
        return dict(name=f.name,
                    content=f.read(),
                    create_date=time.strftime('%d.%M.%Y %H:%M:%S', time.gmtime(os.path.getctime(path))),
                    edit_date=time.strftime('%d.%M.%Y %H:%M:%S', time.gmtime(os.path.getmtime(path))),
                    size=int(os.path.getsize(path)))
except RuntimeError as err:
    e.args += ('Custom message',)
    ...

