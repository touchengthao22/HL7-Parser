from parser.message_parser import parse_message
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datetime import datetime

console = Console()


def print_section(title, content):
    """Pretty print a dictionary as a panel."""
    formatted = "\n".join(f"{k}: {v}" for k, v in content.items())
    console.print(Panel(formatted, title=title, expand=False))


def print_obx_table(obx_list):
    """Pretty table for lab results."""
    table = Table(title="OBX - Lab Results")

    table.add_column("Test", style="cyan")
    table.add_column("Value", style="green")
    table.add_column("Units", style="yellow")
    table.add_column("Reference Range", style="magenta")
    table.add_column('Date')

    for obx in obx_list:
        table.add_row(
            str(obx.get("observation_identifier", "")),
            str(obx.get("observation_value", "")),
            str(obx.get("units", "")),
            str(obx.get("reference_range", "")),
            str(datetime.strptime(obx.get("observation_datetime", ""), "%Y%m%d%H%M"))
        )

    console.print(table)


def main():
    path = "messages/message.hl7"

    console.print("[bold blue]Loading HL7 file...[/bold blue]")

    with open(path, "r") as f:
        text = f.read()

    message = parse_message(text)

    console.print("[bold green]Parsing complete[/bold green]\n")

    # MSH
    print_section("MSH - Message Header", message.msh)

    # PID
    print_section("PID - Patient Information", message.pid)

    # PV1
    print_section("PV1 - Visit Information", message.pv1)

    # OBX
    print_obx_table(message.obx)

    console.print("\n[bold green]Done.[/bold green]")


if __name__ == "__main__":
    main()