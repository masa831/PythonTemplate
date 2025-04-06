from target_src.model import Model


def main():
    print('Hello world')
    model = Model()
    print('BF', model.param.a, model.param.b, model.param.c)
    model.update()
    print('AF', model.param.a, model.param.b, model.param.c)

if __name__ == "__main__":
    main()
