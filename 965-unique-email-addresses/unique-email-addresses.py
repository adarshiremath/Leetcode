class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final = []
        for email in emails:
            local, domain = email.split("@")
            if '+' in local:
                local = local.split('+')[0]
            if '.' in local:
                local = "".join(local.split('.'))
            final.append("@".join([local, domain]))
        return len(set(final))