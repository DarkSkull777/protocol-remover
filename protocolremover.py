import argparse
import os
import sys

putih = '\033[1;97m'
merah = '\033[1;91m'
hijau = '\033[1;92m'
kuning = '\033[1m\033[93m'
biru = '\033[1;94m'
reset = '\033[0m'

def remove_protocols(line, protocols):
    for protocol in protocols:
        line = line.replace(f"{protocol}://", "")
    return line

def main(args):
    protocols = args.protocol.split(',') if args.protocol else []
    
    if not protocols:
        print(f"{merah}No protocol specified for removal.")
        sys.exit(1)

    if args.list:
        if not os.path.isfile(args.list):
            print(f"{merah}File {args.list} does not exist.")
            sys.exit(1)
        
        print(f"{biru}Processing from {args.list}....")
        
        try:
            with open(args.list, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            print(f"{biru}Reading files....")
            print(f"{biru}Files have {len(lines)} lines...")
            
            print(f"{biru}Removing protocol {', '.join(protocols)}....")
            
            with open(args.output, 'w', encoding='utf-8') if args.output else sys.stdout as f_out:
                for line in lines:
                    cleaned_line = remove_protocols(line.strip(), protocols)
                    f_out.write(cleaned_line + '\n')
            
            if args.output:
                print(f"{biru}Success removing protocol....")
                print(f"{biru}Saving results to {args.output}....")
            else:
                print(f"{biru}Success removing protocol....")
            
            print(f"{biru}Done....")
        
        except IOError as e:
            print(f"{merah}Error reading or writing file: {e}")
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove HTTP or HTTPS protocol from file")
    parser.add_argument('-p', '--protocol', required=True, help="Protocols to remove (comma-separated, e.g., 'http,https')")
    parser.add_argument('-l', '--list', required=True, help="File containing list of domains")
    parser.add_argument('-o', '--output', help="File to save the results (default: stdout)")

    args = parser.parse_args()

    if not args.protocol or not args.list:
        parser.print_help()
        sys.exit(1)

    main(args)
