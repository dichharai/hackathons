using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;
using Tweetinvi;
using Tweetinvi.Models;

namespace DataRetrieve
{
    class Program
    {
        static void Main()
        {
            Auth.SetUserCredentials("XXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");

            TweetinviEvents.QueryBeforeExecute += (sender, args) =>
            {
                var queryRateLimits = RateLimit.GetQueryRateLimit(args.QueryURL);

                if (queryRateLimits == null) return;
                if (queryRateLimits.Remaining > 0)return;
                Thread.Sleep((int)queryRateLimits.ResetDateTimeInMilliseconds);
            };
            const string inputFileName = @"biz_name.txt";
            var companies = File.ReadAllLines(inputFileName);

            const string output = @"TwitterOutput.txt";
            foreach (var company in companies)
            {
                var users = Search.SearchUsers(company);
                if (users!=null)
                {
                    var usersList = users as IList<IUser> ?? users.ToList();
                    File.AppendAllText(output,
                        usersList.Any()
                            ? $"{company}\t{usersList[0].ScreenName}\t{usersList[0].StatusesCount}\r\n"
                            : $"{company}\t0\t0\r\n");
                }
                else
                {
                    File.AppendAllText(output, $"{company}\t0\t0\r\n");
                }
            }

            Console.WriteLine(@"END");
            Console.ReadLine();
        }
    }
}