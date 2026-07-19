from oat import read, write


def run(args):
    genome = read(args.input)

    write(genome, args.output)

    print(f"Exported to: {args.output}")