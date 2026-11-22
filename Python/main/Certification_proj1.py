# My 2nd certification project in freeCodeCamp

# Build a Budget App


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            'amount': -amount,
            'description': description
        })
        return True

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        result = f'{self.name:*^30}\n'

        for item in self.ledger:
            description = item['description'][:23]
            result += f'{description:23}{item["amount"]:>7.2f}\n'

        result += f'Total: {self.get_balance()}'
        return result


def create_spend_chart(categories):
    spent_by_category = [
        sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        for category in categories
    ]
    total_spent = sum(spent_by_category)

    if total_spent == 0:
        percentages = [0 for _ in categories]
    else:
        percentages = [
            int(spent / total_spent * 100) // 10 * 10
            for spent in spent_by_category
        ]

    lines = ['Percentage spent by category']

    for level in range(100, -1, -10):
        line = f'{level:>3}| '
        for percentage in percentages:
            line += 'o  ' if percentage >= level else '   '
        lines.append(line)

    lines.append('    ' + '-' * (len(categories) * 3 + 1))

    max_name_length = max((len(category.name) for category in categories), default=0)
    for row in range(max_name_length):
        line = '     '
        for category in categories:
            line += (category.name[row] if row < len(category.name) else ' ') + '  '
        lines.append(line)

    return '\n'.join(lines)
